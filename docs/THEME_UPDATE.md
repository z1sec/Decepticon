# 다크/라이트 모드 테마 개선 사항

## 개요
Decepticon 프로젝트의 다크/라이트 모드 테마 시스템을 전면 개선하여, 사이드바 버튼, 터미널 UI, 채팅 UI에서 테마가 일관되게 적용되도록 수정했습니다.

## 수정된 파일들

### 1. `frontend/theme_manager.py`
**주요 개선사항:**
- 사이드바 버튼 CSS 선택자 강화
- 더 포괄적인 버튼 선택자 추가 (`button`, `.stButton > button`, `[data-baseweb="button"]` 등)
- 터미널 UI와 채팅 UI에 대한 동적 테마 CSS 추가
- 버튼 호버/활성 상태 스타일링 강화

**새로 추가된 기능:**
```css
/* 강화된 사이드바 버튼 선택자 */
section[data-testid="stSidebar"] button,
section[data-testid="stSidebar"] .stButton > button,
section[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"],
/* ... 더 많은 선택자들 */

/* 터미널 테마 오버라이드 */
.terminal-container {
    background-color: {terminal_bg} !important;
    color: {terminal_text} !important;
    /* ... 테마별 색상 적용 */
}

/* 채팅 UI 테마 오버라이드 */
div.stChatMessage[data-testid="stChatMessage"] .stChatMessageContent {
    background-color: {message_bg} !important;
    /* ... 테마별 색상 적용 */
}
```

### 2. `static/css/terminal.css`
**주요 개선사항:**
- 정적 색상을 기본값으로 변경 (다크 모드 기준)
- 모든 색상 요소에 `transition: color 0.3s ease` 추가
- 더 일관된 색상 스키마 적용
- 스크롤바 스타일 개선

**변경된 색상:**
- `terminal-user`: `#FF0000` → `#4EC9B0` (터미널 프롬프트 색상)
- `terminal-command-text`: `#FFFFFF` → `#DCDCAA` (명령어 색상)
- `terminal-output`: `#FFFFFF` → `#CCCCCC` (출력 색상)

### 3. `static/css/chat_ui.css`
**주요 개선사항:**
- 모든 채팅 UI 요소에 `transition` 효과 추가
- 테마 대응을 위한 투명 배경색 설정
- 에이전트별 테두리 색상에 transition 추가

### 4. `static/dark_theme.css` & `static/light_theme.css`
**주요 개선사항:**
- 사이드바 버튼 스타일을 완전히 재작성
- 호버 및 활성 상태 효과 추가
- 일관된 버튼 디자인 적용

**다크 모드 버튼 색상:**
- 배경: `#262730`
- 텍스트: `#FAFAFA`
- 테두리: `#404040`
- 호버 배경: `#404040`
- 활성 배경: `#FF4B4B`

**라이트 모드 버튼 색상:**
- 배경: `#FFFFFF`
- 텍스트: `#31333F`
- 테두리: `#DFE2E6`
- 호버 배경: `#E8EAF0`
- 활성 배경: `#FF4B4B`

### 5. `app.py`
**주요 개선사항:**
- 사이드바 버튼에 고유 `key` 추가
- CSS 선택자 매칭을 위한 버튼 식별자 개선

## 테마 시스템 작동 방식

### 1. 테마 전환 과정
1. 사용자가 테마 토글 버튼 클릭
2. `theme_manager.toggle_theme()` 호출
3. `st.session_state.dark_mode` 상태 변경
4. `.streamlit/config.toml` 파일 업데이트
5. `apply_theme()` 메서드로 즉시 CSS 적용
6. `st.rerun()`으로 페이지 새로고침

### 2. CSS 적용 순서
1. 기본 테마 CSS (`dark_theme.css` 또는 `light_theme.css`)
2. 사이드바 및 기본 UI 오버라이드 CSS
3. 터미널 테마 오버라이드 CSS
4. 채팅 UI 테마 오버라이드 CSS
5. 레이아웃 CSS
6. 모델 정보 CSS
7. 입력창 고정 CSS

### 3. 색상 변수 시스템
테마별로 동적으로 생성되는 색상 변수들:
```python
# 사이드바 색상
sidebar_bg = "#0B0B12" if theme == "dark" else "#F0F2F6"
sidebar_text = "#FAFAFA" if theme == "dark" else "#31333F"

# 버튼 색상
button_bg = "#262730" if theme == "dark" else "#FFFFFF"
button_text = "#FAFAFA" if theme == "dark" else "#31333F"

# 터미널 색상
terminal_bg = "#1E1E1E" if theme == "dark" else "#F5F5F5"
terminal_text = "#FFFFFF" if theme == "dark" else "#333333"

# 그 외 다양한 UI 요소별 색상들...
```

## 해결된 문제들

### 1. 사이드바 버튼 테마 미적용
**문제:** Change Model, Chat History, New Chat 버튼이 테마 변경에 반응하지 않음
**해결:** 더 구체적이고 포괄적인 CSS 선택자 사용

### 2. 터미널 UI 정적 색상
**문제:** 터미널이 항상 동일한 색상으로 표시됨
**해결:** 테마별 동적 색상 적용 및 transition 효과 추가

### 3. 채팅 UI 일부 요소 테마 미적용
**문제:** 채팅 메시지 배경, 헤더 등이 테마 변경에 반응하지 않음
**해결:** 채팅 UI 전용 테마 오버라이드 CSS 추가

## 테스트 방법

1. **테마 전환 테스트:**
   - 사이드바의 테마 토글 버튼 클릭
   - 모든 UI 요소가 즉시 테마에 맞게 변경되는지 확인

2. **사이드바 버튼 테스트:**
   - "🔁 Change Model", "💬 Chat History", "✨ New Chat" 버튼의 색상 확인
   - 호버 및 클릭 시 색상 변화 확인

3. **터미널 UI 테스트:**
   - 터미널 명령어 실행 후 배경색, 텍스트 색상 확인
   - 프롬프트, 명령어, 출력 색상이 테마에 맞는지 확인

4. **채팅 UI 테스트:**
   - AI 에이전트 메시지 배경색 확인
   - 코드 블록 색상 확인
   - 에이전트 헤더 색상 확인

## 향후 개선 사항

1. **애니메이션 효과 강화:** 더 부드러운 테마 전환 애니메이션
2. **커스텀 색상 지원:** 사용자가 직접 색상을 설정할 수 있는 기능
3. **시스템 테마 감지:** OS의 다크/라이트 모드 설정 자동 감지
4. **접근성 개선:** 고대비 모드 지원

## 기술적 세부사항

### CSS 우선순위 전략
- `!important` 선언을 전략적으로 사용하여 Streamlit 기본 스타일 오버라이드
- CSS 선택자 명시도(specificity)를 높여 안정적인 스타일 적용
- 여러 선택자를 조합하여 다양한 DOM 구조에 대응

### 성능 최적화
- CSS transition으로 부드러운 테마 전환 (0.3초)
- 테마 변경 시 필요한 부분만 업데이트
- CSS 파일 분리로 유지보수성 향상

### 호환성
- 다양한 브라우저에서 일관된 스타일 적용
- Streamlit 버전 업데이트 대응을 위한 유연한 선택자 구조
