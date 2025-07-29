# CLI-Me-Codex5

이 저장소는 파이썬 개발자가 자신의 프로필을 간단히 소개할 수 있는 CLI 도구 예제를 포함합니다.

## 실행 방법

```bash
python developer/cli-proflie.py
```

`DATA_FILE` 환경 변수를 설정하면 기본 `data.json` 대신 다른 경로의 데이터를 사용할 수 있습니다.

## 의존성 관리

프로젝트는 [Rye](https://github.com/astral-sh/rye)를 통해 의존성을 관리하는 것을 권장합니다.

```
rye sync
```

## 코드 스타일 검사

[Ruff](https://github.com/astral-sh/ruff)를 사용하여 코드 스타일을 확인할 수 있습니다.

```
ruff .
```

## 데이터 수정 방법

`developer/data.json` 파일을 열어 자신의 이니셜, 자기소개, 기술 스택을 수정하세요.

