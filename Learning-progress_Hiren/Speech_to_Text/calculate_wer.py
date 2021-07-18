import jiwer

correct_text = ""
with open('orignal-text.txt', 'r') as fin:
    correct_text = fin.read()

my_text = ""
with open("my_speech_output.txt", "r") as fin1:
    my_text = fin1.read()

ground_truth = correct_text
hypothesis = my_text

ground_truth = ground_truth.replace('.', '')
ground_truth = ground_truth.lower()
error = jiwer.wer(ground_truth, hypothesis)

print(ground_truth)
print("-----------------------------------------------------------------------------------------------------------------------------------------------")
print(hypothesis)
print("WER rate is: {}".format(error))
