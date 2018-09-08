# `__new__` 함수 알아 보기
- django rest framework 에서 serializer 에서 `__new__` 사용 하는 결을 보고 어떤 것 인지 궁금해 테스트 작성

## 테스트 내용
- `__new__` 에서 아무것도 리턴 하지 않으면 어떻게 될까?
    - 생성자로 호출지 `None` 이 리턴되며, `__init__` 메서드가 호출 되지 않는다.
- 상속에서 `__new__` 호출 시 어떤 순서로 호출 될까? (부모 -> 자식 아니면 자식 -> 부모)
    - 자식 -> 부모 순으로 호출 되며, 다중 상속인 경우를 위해 `super().__new__()` 가 권장 되는 것 같음
- `__new__` 로 factory 패턴을 어떻게 구현 할 수 있을까?
    - `__new__` 에서 인지 하나를 받아 그 인자로 맞는 자식 클래스를 `__new__` 한다.
    - 자식 생성자를 호출 하는 것보다 `super().__new__` 하면 재귀의 위험을 방지 할 수 있고, 다중 상속이 깨지지 않을 수 있기에 권장 됨