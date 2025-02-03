import time
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
class AIInterviewer:
    def __init__(self):
        # A sample list of interview questions.
        self.questions = [
            "Tell me about yourself.",
            "What are your greatest strengths?",
            "What are your biggest weaknesses?",
            "Describe a challenging situation at work and how you overcame it.",
            "Where do you see yourself in five years?",
            "Why are you interested in this position?",
            "How do you handle stress and pressure?",
            "Can you tell me about a time when you failed, and what you learned from it?"
        ]
        self.responses = []
        self.sia = SentimentIntensityAnalyzer()

    def start_interview(self):
        print("\nWelcome to the AI Interview Simulator!")
        print("I will ask you a series of questions. Try to answer as you would in a real interview.\n")
        time.sleep(1)
        
        for idx, question in enumerate(self.questions, start=1):
            print(f"Interviewer ({idx}/{len(self.questions)}): {question}")
            user_response = input("You: ")
            self.responses.append(user_response)
            print("Processing your response...\n")
            time.sleep(1)  

        self.provide_feedback()

    def provide_feedback(self):
        print("\n=== Interview Summary & Detailed Feedback ===\n")
        for idx, (question, response) in enumerate(zip(self.questions, self.responses), start=1):
            sentiment = self.sia.polarity_scores(response)
            word_count = len(response.split())
            sentences = [s for s in response.split('.') if s.strip()]
            sentence_count = len(sentences)
            
            print(f"Question {idx}: {question}")
            print(f"Your response: {response}")
            print(f"Word count: {word_count}")
            print(f"Sentence count: {sentence_count}")
            print(f"Sentiment Analysis: {sentiment}")
            print("\nFeedback:")

            # Detailed feedback based on word count
            if word_count < 10:
                print("- Your answer is very brief. In an interview, it's important to provide sufficient detail so that your thought process and expertise are clear.")
                print("- Consider expanding on your answer with specific examples, challenges faced, and the lessons learned from those experiences.")
                print("- A longer, more descriptive answer can help demonstrate your problem-solving abilities and communication skills.")
            elif word_count < 20:
                print("- Your answer is concise, which can be a strength, but it may also leave the interviewer wanting more detail.")
                print("- Try to add more context by elaborating on key points and offering concrete examples.")
                print("- Think about the STAR method (Situation, Task, Action, Result) to structure your response and provide a comprehensive narrative.")
            else:
                print("- Your response is sufficiently detailed, showing that you are comfortable elaborating on your experiences.")
                print("- Ensure that all details are relevant to the question and help highlight your key strengths and problem-solving abilities.")
                print("- While detail is good, make sure you stay on topic and avoid unnecessary digressions.")

            # Detailed feedback based on sentiment analysis
            if sentiment['compound'] < -0.2:
                print("- The overall tone of your response appears a bit negative.")
                print("- In interviews, it's beneficial to frame challenges or setbacks as learning opportunities. Emphasize what you learned from difficult situations and how you improved as a result.")
                print("- Try to avoid overly negative language; instead, focus on how you turned a challenge into a success.")
            elif sentiment['compound'] > 0.5:
                print("- Your response carries a highly positive and enthusiastic tone, which is great for showing passion and energy.")
                print("- However, be cautious that your enthusiasm does not come off as unrealistic. Balance your positivity with concrete examples and critical analysis.")
                print("- Make sure your response also includes moments of reflection or areas where you faced challenges, to present a well-rounded picture of your experience.")
            else:
                print("- Your tone is balanced and professional, which is ideal in an interview setting.")
                print("- Maintaining a neutral tone while incorporating personal insights and examples helps in presenting an authentic and credible answer.")
                print("- Continue to support your responses with both achievements and reflections on areas for improvement.")

            # Additional feedback based on sentence structure
            if sentence_count < 2:
                print("- Your response could benefit from a clearer structure. Consider breaking your answer into multiple sentences to organize your ideas better.")
                print("- A well-structured answer might include an introduction, a detailed explanation or example, and a concluding sentence that ties everything together.")
                print("- This approach not only improves clarity but also helps the interviewer follow your thought process more easily.")
            elif sentence_count > 5:
                print("- Your answer is quite elaborate, which shows that you have a lot to share.")
                print("- However, be careful not to overwhelm the interviewer with too many details. Focus on the most impactful aspects of your experience.")
                print("- Try to condense your points and remove any redundant or less relevant information, ensuring that your key messages remain clear.")
            else:
                print("- Your sentence structure is well-balanced, providing enough detail without becoming overly verbose.")
                print("- This indicates that you have a good grasp on organizing your thoughts logically and clearly.")
                print("- Continue to aim for clarity and conciseness while still providing sufficient context for your responses.")

            print("-" * 60)
        
        print("Thank you for participating in the AI Interview Simulator. Use this feedback to refine your responses and best of luck with your upcoming interviews!")

if __name__ == "__main__":
    interviewer = AIInterviewer()
    interviewer.start_interview()
