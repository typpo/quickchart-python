"""A Python client for quickchart.io, a web service that generates static
charts."""

from __future__ import annotations

import datetime
import json
import re
from importlib import metadata
from typing import Any, Optional, Union
from urllib.parse import urlencode

import requests

try:
    __version__ = metadata.version("quickchart.io")
except metadata.PackageNotFoundError:  # pragma: no cover
    # Package is not installed (e.g. running from a source checkout).
    __version__ = "0.0.0"

USER_AGENT = f"quickchart-python ({__version__})"

FUNCTION_DELIMITER_RE = re.compile(r'"__BEGINFUNCTION__(.*?)__ENDFUNCTION__"')


class QuickChartFunction:
    def __init__(self, script: str):
        self.script = script

    def __repr__(self) -> str:
        return self.script


def serialize(obj: Any) -> Any:
    if isinstance(obj, QuickChartFunction):
        return "__BEGINFUNCTION__" + obj.script + "__ENDFUNCTION__"
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    return obj.__dict__


def dump_json(obj: Any) -> str:
    ret = json.dumps(obj, default=serialize, separators=(",", ":"))
    ret = FUNCTION_DELIMITER_RE.sub(
        lambda match: json.loads('"' + match.group(1) + '"'), ret
    )
    return ret


class QuickChart:
    def __init__(self) -> None:
        self.config: Optional[Union[dict, str]] = None
        self.width: int = 500
        self.height: int = 300
        self.background_color: str = "#ffffff"
        self.device_pixel_ratio: float = 1.0
        self.format: str = "png"
        self.version: str = "2.9.4"
        self.key: Optional[str] = None
        self.scheme: str = "https"
        self.host: str = "quickchart.io"
        self.timeout: Optional[float] = 60.0

    def is_valid(self) -> bool:
        return self.config is not None

    def get_url_base(self) -> str:
        return f"{self.scheme}://{self.host}"

    def _serialized_config(self) -> str:
        return dump_json(self.config) if isinstance(self.config, dict) else self.config

    def get_url(self) -> str:
        if not self.is_valid():
            raise RuntimeError(
                "You must set the `config` attribute before generating a url"
            )
        params = {
            "c": self._serialized_config(),
            "w": self.width,
            "h": self.height,
            "bkg": self.background_color,
            "devicePixelRatio": self.device_pixel_ratio,
            "f": self.format,
            "v": self.version,
        }
        if self.key:
            params["key"] = self.key
        return f"{self.get_url_base()}/chart?{urlencode(params)}"

    def _post(self, url: str) -> requests.Response:
        postdata = {
            "chart": self._serialized_config(),
            "width": self.width,
            "height": self.height,
            "backgroundColor": self.background_color,
            "devicePixelRatio": self.device_pixel_ratio,
            "format": self.format,
            "version": self.version,
        }
        if self.key:
            postdata["key"] = self.key
        headers = {
            "user-agent": USER_AGENT,
        }
        resp = requests.post(url, json=postdata, headers=headers, timeout=self.timeout)
        if resp.status_code != 200:
            err_description = resp.headers.get("x-quickchart-error")
            detail = f"\n{err_description}" if err_description else ""
            raise RuntimeError(
                "Invalid response code from chart creation endpoint: "
                f"{resp.status_code}{detail}"
            )
        return resp

    def get_short_url(self) -> str:
        resp = self._post(f"{self.get_url_base()}/chart/create")
        parsed = json.loads(resp.text)
        if not parsed["success"]:
            raise RuntimeError("Chart creation endpoint failed to create chart")
        return parsed["url"]

    def get_bytes(self) -> bytes:
        resp = self._post(f"{self.get_url_base()}/chart")
        return resp.content

    def to_file(self, path: str) -> None:
        content = self.get_bytes()
        with open(path, "wb") as f:
            f.write(content)
