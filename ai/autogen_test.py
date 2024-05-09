from autogen import  UserProxyAgent, config_list_from_json, AssistantAgent, GroupChat, GroupChatManager


def main():
    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample.
    # For example, if you have created a OAI_CONFIG_LIST file in the current working directory, that file will be used.
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

    llm_config = {"config_list": config_list, "cache_seed": 42}
    user_proxy = UserProxyAgent(
        name="User_proxy",
        system_message="A human admin.",
        code_execution_config={
            "last_n_messages": 2,
            "work_dir": "groupchat",
            "use_docker": False,
        },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
        human_input_mode="TERMINATE",
    )
    coder = AssistantAgent(
        name="Coder",
        llm_config=llm_config,
    )
    pm = AssistantAgent(
        name="Product_manager",
        system_message="Creative in software product ideas.",
        llm_config=llm_config,
    )
    groupchat = GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    user_proxy.initiate_chat(
    manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
)


if __name__ == "__main__":
    main()