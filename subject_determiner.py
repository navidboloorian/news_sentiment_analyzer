from ollama import chat

def determine_subject(headlines):
  prompt = """
    Given the following headline, determine the subject. 
    Respond with only the subject name, no explanation or introduction is necessary (i.e. don't do subject: [subject name]).
    The list of possible subjects includes and is limited to: 'Biden', 'Harris', 'Trump', 'Republicans', 'Democrats'.
    The subject doesn't necessarily need to be direct. For instance, if a headline contains 'Mitch McConnell' that can be grouped as 'Republicans'. 
    If a headline doesn't fall into any of these categories, return 'N/A'.
    A headline shouldn't be classified with multiple subjects, individuals take precedence over party.
    Here is the headline:
  """

  valid_subjects = set(['Biden', 'Harris', 'Trump', 'Republicans', 'Democrats'])
  subjects = []

  for headline in headlines:
    response = chat(
      model="llama3.2",
      messages=[
        {
          "role": "user",
          "content": f"{prompt}{headline}"
        }
      ]
    )

    subject = response.message.content

    if subject != "N/A" and subject not in valid_subjects:
      subject = "N/A"

    subjects.append(subject)

  return subjects
  
