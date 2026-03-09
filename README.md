# My Boilerplate Collection

개인 보일러플레이트 및 코드 레퍼런스 모음 저장소.  
자주 사용하는 기술 스택의 템플릿, 외부 서비스 연동 레시피, 풀스택 조합 예제를 한 곳에서 관리한다.

> **이 저장소의 목적**: 새 프로젝트를 시작할 때 필요한 폴더를 복사해서 즉시 사용할 수 있는 **독립 실행 가능한** 보일러플레이트 모음집.

---

## 폴더 구조

```
my_boilerplate/
├── foundation/       # 단일 기술 기반 템플릿
├── integrations/     # 외부 서비스 연동 레시피
├── stacks/           # 풀스택 조합 템플릿
├── snippets/         # 재사용 가능한 코드 조각 / 치트시트
└── lab/              # 일회성 실험 코드 (언제든 삭제 가능)
```

---

## foundation/

단일 기술·프레임워크의 기본 뼈대. 각 폴더가 독립적으로 실행 가능하다.

| 폴더 | 설명 | 주요 기술 |
|------|------|-----------|
| `foundation/fastapi/` | FastAPI REST API 보일러플레이트 | Python, FastAPI, Loguru, uv |

### foundation/fastapi 포함 내용
- Loguru 기반 로깅 설정
- 요청/응답 로깅 미들웨어 (request_id 추적)
- CORS 설정 분리
- 전역 예외 핸들러 및 커스텀 예외 클래스
- 표준 라우터 구조

---

## integrations/

외부 서비스·API 연동에 필요한 코드를 독립 모듈로 정리한다.

| 폴더 | 설명 | 상태 |
|------|------|------|
| *(예정)* `integrations/azure-blob/` | Azure Blob Storage 업로드/다운로드 | 🔲 |
| *(예정)* `integrations/jira/` | Jira REST API 연동 | 🔲 |
| *(예정)* `integrations/collab/` | Collab 연동 | 🔲 |

---

## stacks/

여러 기술을 조합한 풀스택 프로젝트 템플릿. `foundation/`의 코드를 기반으로 확장한다.

| 폴더 | 설명 | 상태 |
|------|------|------|
| *(예정)* `stacks/fastapi-nuxt/` | FastAPI + Nuxt.js 풀스택 | 🔲 |
| *(예정)* `stacks/fastapi-langgraph/` | FastAPI + LangGraph AI 에이전트 | 🔲 |

---

## snippets/

자주 쓰는 코드 패턴, 유틸리티 함수, 설정 예제 등 작은 단위의 참고 코드를 모아둔다.

---

## lab/

실험·학습 목적의 임시 코드. 결과물이 정리되면 적절한 폴더로 승격시키고, 아니면 삭제한다.  
**이 폴더의 내용은 언제든 삭제될 수 있다.**

---

## 사용 방법

```bash
# 예: FastAPI 보일러플레이트를 새 프로젝트로 복사
cp -r foundation/fastapi/ ~/projects/my-new-api/

# 의존성 설치 후 실행
cd ~/projects/my-new-api/
uv sync
uv run uvicorn src.main:app --port=8081 --reload --host 0.0.0.0
```

## 컨벤션

- 각 보일러플레이트는 **자체 의존성 파일**(pyproject.toml, package.json 등)을 갖는다.
- 각 보일러플레이트 폴더 안에 개별 `README.md`를 두어 해당 템플릿의 사용법을 설명한다.
- 루트 `.gitignore` 하나로 Python / Node.js / 기타 공통 패턴을 모두 커버한다.
