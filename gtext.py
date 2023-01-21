from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


tokenizer = AutoTokenizer.from_pretrained("huggingtweets/animemajg")
model = AutoModelForCausalLM.from_pretrained("huggingtweets/animemajg")


def gen_rei_text(text):
    inputs = tokenizer.encode(text, return_tensors='pt')

    outputs = model.generate(
        inputs, max_length=200, do_sample=True
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text


if __name__ == "__main__":
    txt = gen_rei_text("hello, i love you")
    print(txt)
