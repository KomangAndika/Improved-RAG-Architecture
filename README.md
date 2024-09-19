# Improved-RAG-Architecture
Using LangChain as the framework
Improved RAG Architecture from my previous project, such as
1. Rather than running the model localy. I'd rather using API from together.ai so I don't destroy my laptop in doing so. (they also provide better model so the outcome of the prompt is wayyyy better). I could also tune the parameter of the LLM for better outcome or maybe model selection for my specific use case.
2. Fixing the chunking problem by using LLM (Semantic Chunker) as the chunker rather than manual chunking.
3. Rewrite the query using LLM before turning it into vector for retrieval purpose for better retrieval.
4. Using both Semantic Search (Context) and Lexical Search (Keyword) for the vector DB, which is FAISS (Facebook AI Similarity Search).
5. Reranking+autocut Algorithm after the retrieval for better output.

RAGAS could also be implemented in this project, a RAG architecture benchmarking
There are other method of RAG I really interested in like GraphRAG.


P.S.
- My semantic chunker run verrry slow, i advise you just use normal text splitter with fixed size and overlap for faster performance
- If you don't want to host the db in local, you can use services like Pinecone or MongoDB Atlas and create a cluster
- I advise you to use other model for the inference and rewriter, find the best one for your usecase
Skibidi
