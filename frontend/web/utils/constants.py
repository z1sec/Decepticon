"""
상수 정의 (리팩토링됨)
애플리케이션 전체에서 사용되는 상수들
"""

# 아이콘 및 이미지 경로
ICON = "assets/logo.png"
ICON_TEXT = "assets/logo_text1.png"

# 기본 설정값
DEFAULT_CHAT_HEIGHT = 700
DEFAULT_THEME = "dark"
DEFAULT_DOCKER_CONTAINER = "decepticon-kali"

# 메시지 타입
MESSAGE_TYPE_USER = "user"
MESSAGE_TYPE_AI = "ai"
MESSAGE_TYPE_TOOL = "tool"

# 에이전트 이름
AGENT_PLANNER = "planner"
AGENT_RECONNAISSANCE = "reconnaissance"
AGENT_INITIAL_ACCESS = "initial_access"
AGENT_EXECUTION = "execution"
AGENT_PERSISTENCE = "persistence"
AGENT_PRIVILEGE_ESCALATION = "privilege_escalation"
AGENT_DEFENSE_EVASION = "defense_evasion"
AGENT_SUMMARY = "summary"

# 에이전트 정보
AGENTS_INFO = [
    {"id": AGENT_PLANNER, "name": "Planner", "icon": "🧠"},
    {"id": AGENT_RECONNAISSANCE, "name": "Reconnaissance", "icon": "🔍"},
    {"id": AGENT_INITIAL_ACCESS, "name": "Initial Access", "icon": "🔑"},
    {"id": AGENT_EXECUTION, "name": "Execution", "icon": "💻"},
    {"id": AGENT_PERSISTENCE, "name": "Persistence", "icon": "🔐"},
    {"id": AGENT_PRIVILEGE_ESCALATION, "name": "Privilege Escalation", "icon": "🔒"},
    {"id": AGENT_DEFENSE_EVASION, "name": "Defense Evasion", "icon": "🕵️"},
    {"id": AGENT_SUMMARY, "name": "Summary", "icon": "📋"},
]

# CSS 클래스 이름
CSS_CLASS_AGENT_STATUS = "agent-status"
CSS_CLASS_STATUS_ACTIVE = "status-active"
CSS_CLASS_STATUS_COMPLETED = "status-completed"
CSS_CLASS_TERMINAL_CONTAINER = "terminal-container"
CSS_CLASS_MAC_TERMINAL_HEADER = "mac-terminal-header"

# 세션 상태 키
SESSION_KEY_EXECUTOR_READY = "executor_ready"
SESSION_KEY_CURRENT_MODEL = "current_model"
SESSION_KEY_WORKFLOW_RUNNING = "workflow_running"
SESSION_KEY_STRUCTURED_MESSAGES = "structured_messages"
SESSION_KEY_TERMINAL_MESSAGES = "terminal_messages"
SESSION_KEY_ACTIVE_AGENT = "active_agent"
SESSION_KEY_COMPLETED_AGENTS = "completed_agents"
SESSION_KEY_TERMINAL_HISTORY = "terminal_history"
SESSION_KEY_DEBUG_MODE = "debug_mode"
SESSION_KEY_THEME_MANAGER = "theme_manager"
SESSION_KEY_REPLAY_MODE = "replay_mode"

# API 키 목록
API_KEYS = [
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY", 
    "OPENROUTER_API_KEY"
]

# 지원되는 프로바이더
PROVIDERS = [
    "Anthropic",
    "OpenAI", 
    "DeepSeek",
    "Gemini",
    "Groq",
    "Ollama",
    "Custom"
]

# 터미널 명령어 정리 프리픽스
TERMINAL_PREFIXES_TO_REMOVE = [
    'Running command:',
    'Executing:',
    'Command:',
    'Execute:',
    '$',
    '# '
]

# 터미널 도구 식별 키워드
TERMINAL_TOOL_KEYWORDS = [
    "terminal",
    "command", 
    "exec",
    "shell"
]

# 링크
COMPANY_LINK = "https://purplelab.framer.ai"

# 파일 경로
CSS_PATH_TERMINAL = "frontend/static/css/terminal.css"
CSS_PATH_CHAT_UI = "frontend/static/css/chat_ui.css"
CSS_PATH_AGENT_STATUS = "frontend/static/css/agent_status.css"
CSS_PATH_LAYOUT = "frontend/static/css/layout.css"
CSS_PATH_INPUT_FIX = "frontend/static/css/input_fix.css"
CSS_PATH_MODEL_INFO = "frontend/static/css/model_info.css"
