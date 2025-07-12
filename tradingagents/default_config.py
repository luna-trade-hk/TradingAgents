import os

# DEFAULT_CONFIG = {
#     "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#     "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
#     "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
#     "data_cache_dir": os.path.join(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#         "dataflows/data_cache",
#     ),
#     # LLM settings
#     "llm_provider": "openai",
#     "deep_think_llm": "o4-mini",
#     "quick_think_llm": "gpt-4o-mini",
#     "backend_url": "https://api.openai.com/v1",
#     # Debate and discussion settings
#     "max_debate_rounds": 1,
#     "max_risk_discuss_rounds": 1,
#     "max_recur_limit": 100,
#     # Tool settings
#     "online_tools": True,
# }

###############
# user config #
###############
# LM STUDIO
# DEFAULT_CONFIG = {
#     "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#     "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
#     "data_dir": os.getenv("TRADINGAGENTS_DATA_DIR", "./data"),
#     "data_cache_dir": os.path.join(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
#         "dataflows/data_cache", 
#     ),
#     # LLM settings
#     "llm_provider": "ollama",
#     "deep_think_llm": "deepseek/deepseek-r1-0528-qwen3-8b",
#     "quick_think_llm": "qwen_qwen3-8b",
#     "backend_url": "http://127.0.0.1:1234/v1",
#     # Debate and discussion settings
#     "max_debate_rounds": 1,
#     "max_risk_discuss_rounds": 1,
#     "max_recur_limit": 100,
#     # Tool settings
#     "online_tools": True,
# }

# Openrouter
DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": os.getenv("TRADINGAGENTS_DATA_DIR", "./data"),
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache", 
    ),
    # LLM settings
    "llm_provider": "openrouter",
    "deep_think_llm": "deepseek/deepseek-r1-0528:free",
    "quick_think_llm": "deepseek/deepseek-chat-v3-0324:free",
    "backend_url": "https://openrouter.ai/api/v1",
    # Embedding settings
    "embedding_url": "http://localhost:1234/v1",
    "embedding": "text-embedding-nomic-embed-text-v1.5",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
