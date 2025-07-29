"""CLI 환경에서 개발자 정보를 출력하는 도구.

Usage:
    python developer/cli-proflie.py

환경 변수:
    DATA_FILE: 데이터 파일 경로를 지정합니다. 기본값은 현재 디렉터리의 data.json 입니다.
"""

import json
import logging
import os
from dataclasses import dataclass
from typing import List

import click
from rich.console import Console
from rich.table import Table
from pyfiglet import Figlet


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Skill:
    기술: str
    수준: str


@dataclass
class DeveloperProfile:
    initials: str
    intro: str
    skills: List[Skill]

    @staticmethod
    def load(path: str) -> "DeveloperProfile":
        """JSON 파일에서 개발자 정보를 읽어 객체로 변환합니다."""
        logger.debug("프로필 로드 경로: %s", path)
        try:
            with open(path, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except FileNotFoundError as exc:
            logger.error("데이터 파일을 찾을 수 없습니다: %s", path)
            raise exc
        except json.JSONDecodeError as exc:
            logger.error("JSON 파싱 오류: %s", exc)
            raise exc

        skills = [Skill(**s) for s in data.get("skills", [])]
        return DeveloperProfile(
            initials=data.get("initials", ""),
            intro=data.get("intro", ""),
            skills=skills,
        )


def render_profile(profile: DeveloperProfile) -> None:
    """Rich와 pyfiglet을 활용해 프로필을 출력합니다."""
    console = Console()

    figlet = Figlet(font="slant")
    console.print(figlet.renderText(profile.initials))

    console.print(f"[bold green]{profile.intro}[/bold green]")

    table = Table(title="기술 스택")
    table.add_column("기술", style="cyan")
    table.add_column("수준", style="magenta")

    for skill in profile.skills:
        table.add_row(skill.기술, skill.수준)

    console.print(table)


@click.command()
def main() -> None:
    """명령행 인터페이스 엔트리포인트."""
    data_path = os.getenv("DATA_FILE", os.path.join(os.path.dirname(__file__), "data.json"))
    logger.info("데이터 파일 경로: %s", data_path)

    try:
        profile = DeveloperProfile.load(data_path)
        render_profile(profile)
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception("프로필을 표시하는 중 오류 발생: %s", exc)
        click.echo("오류가 발생했습니다. 로그를 확인해주세요.")


if __name__ == "__main__":
    main()
