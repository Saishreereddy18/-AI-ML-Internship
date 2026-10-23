# Day 15 – Large Language Models (LLMs)

**Internship:** Linkific AI/ML Internship  
**Day:** 15  
**Topic:** Large Language Models and Model Comparison

## 1. Objective

To understand Large Language Models (LLMs), learn how modern AI applications use them, and experiment with pretrained models from Hugging Face.

## 2. Learning Objectives

- Understand the evolution of AI from Machine Learning to Generative AI.
- Learn the basics of Large Language Models.
- Explore the Hugging Face Model Hub.
- Test text generation, sentiment analysis, and summarization models.
- Compare model outputs and identify the suitable model for each task.

## 3. Tools and Technologies

- Python
- Hugging Face Transformers
- PyTorch
- Pandas
- Jupyter Notebook
- Hugging Face Model Hub

## 4. Models Tested

| Model                                                        | Task               | Purpose                                   |
| ------------------------------------------------------------ | ------------------ | ----------------------------------------- |
| `distilgpt2`                                                 | Text Generation    | Generates text from an input prompt.      |
| `distilbert/distilbert-base-uncased-finetuned-sst-2-english` | Sentiment Analysis | Classifies text as positive or negative.  |
| `facebook/bart-large-cnn`                                    | Summarization      | Produces a shorter summary of an article. |

## 5. Model Comparison

- **DistilGPT-2:** Useful for generating text continuations.
- **DistilBERT:** Useful for identifying sentiment in sentences.
- **BART Large CNN:** Useful for summarizing longer passages.

Each model is designed for a different task. The most suitable model depends on the intended application.

## 6. Conclusion

This task provided practical experience with pretrained language models and demonstrated how Hugging Face Transformers can support different NLP applications. The experiments illustrated text generation, sentiment classification, and text summarization.

## 7. References

- [Hugging Face Model Hub](https://huggingface.co/models)
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [DistilGPT-2](https://huggingface.co/distilbert/distilgpt2)
- [DistilBERT Sentiment Analysis](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
- [BART Large CNN](https://huggingface.co/facebook/bart-large-cnn)
