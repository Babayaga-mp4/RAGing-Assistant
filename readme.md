This is a fun little project that I've explored to primarily get familiarized with various RAG strategies. The current iteration of the project can:

    - Handle large pdfs (Out of the box pdf chunking)
    - Can Stream response realtime onto the terminal.
    - Can hold conversations based on chat history.
    - Supports local LLMs
    - Supports OpenAI (BYOL)

The main motivation was to keep this RAG as decoupled as possible from Langchain or similar LLM frameworks. This project will keep recieving upgrades both logical and architectural for the foreseable future, or until its probably over engineered. 


You can simply clone the repo, spin up the docker and hit the following command:

 `python main.py docs/NIPS-2017-attention-is-all-you-need-Paper.pdf`

This would get it up and running.

If you're more of a Community person, you'd probably have your own LLM in which case you'd want to head over to the docker-compose uncomment the ollama services and make sure to check the `configurations.py` file.