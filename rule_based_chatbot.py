import random

# 1. Dictionary of responses

responses = {
    "hello": [
        "Hello!",
        "Hi there!",
        "Hey! How can I help you?"
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine, thanks for asking!",
        "I'm ready to help you learn AI!"
    ],

    "your name": [
        "I'm your Rule-Based AI Chatbot.",
        "You can call me AI-Bot."
    ],

    "ai": [
        "AI stands for Artificial Intelligence. It is the field of creating systems that can perform tasks requiring human-like intelligence."
    ],

    "ml": [
        "Machine Learning is a subset of AI where computers learn patterns from data."
    ],

    "dl": [
        "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers."
    ],

    "intelligent agent": [
        "An intelligent agent perceives its environment through sensors and takes actions through actuators to achieve a goal."
    ],

    "bfs": [
        "BFS stands for Breadth-First Search. It explores a tree or graph level by level and typically uses a Queue."
    ],

    "dfs": [
        "DFS stands for Depth-First Search. It explores as deeply as possible before backtracking and uses a Stack or recursion."
    ],

    "rational agent": [
        "A rational agent is an agent that chooses the action expected to maximize its performance measure based on its percept history and available knowledge."
    ],

    "peas": [
        "PEAS stands for Performance measure, Environment, Actuators, and Sensors. It is used to specify an intelligent agent's task environment."
    ],

    "ucs": [
        "Uniform Cost Search explores the node with the lowest path cost first. It uses a priority queue and is optimal when step costs are non-negative."
    ],

    "greedy": [
        "Greedy Best First Search selects the node that appears closest to the goal according to a heuristic function h(n). It is not guaranteed to find the optimal solution."
    ],

    "a star": [
        "A* Search uses f(n) = g(n) + h(n), where g(n) is the cost from the start node and h(n) is the estimated cost to the goal. It can find an optimal solution when the heuristic is admissible."
    ]
}


# 2. Help function

def show_help():
    print("\nAvailable commands:")
    print("  hello")
    print("  how are you")
    print("  your name")
    print("  what is AI")
    print("  what is ML")
    print("  what is DL")
    print("  intelligent agent")
    print("  rational agent")
    print("  PEAS")
    print("  BFS")
    print("  DFS")
    print("  Uniform Cost Search")
    print("  Greedy Best First Search")
    print("  A*")
    print("  history")
    print("  quiz")
    print("  help")
    print("  bye")


# 3. Random response function

def random_response(category):
    return random.choice(responses[category])


# 4. Quiz function

def start_quiz():

    questions = [
        {
            "question": "What does BFS use?",
            "answer": "queue"
        },
        {
            "question": "What does DFS use?",
            "answer": "stack"
        },
        {
            "question": "What does PEAS stand for?",
            "answer": "performance measure, environment, actuators, sensors"
        },
        {
            "question": "What is the evaluation function used by A*?",
            "answer": "f(n) = g(n) + h(n)"
        },
        {
            "question": "Which search algorithm selects the node with the lowest path cost?",
            "answer": "uniform cost search"
        }
    ]

    quiz = random.choice(questions)

    print("\nQuiz Time!")
    print(quiz["question"])

    user_answer = input("Your answer: ").lower().strip()

    if user_answer == quiz["answer"]:
        print("Bot: Correct!")
    else:
        print("Bot: Not quite.")
        print("Correct answer:", quiz["answer"])


# 5. Chatbot function

def chatbot():

    history = []

    print("Welcome to your AI Study Chatbot!")
    print("Type 'help' to see what I can answer.")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower().strip()

        history.append("You: " + user_input)

        # Help

        if user_input == "help":
            show_help()
            continue

        # Quiz

        elif user_input == "quiz":
            start_quiz()
            continue

        # Conversation history

        elif user_input == "history":

            print("\nConversation History:")

            for message in history:
                print(message)

            continue

        # Exit

        elif user_input == "bye":

            response = random.choice([
                "Goodbye!",
                "See you later!",
                "Keep learning AI!"
            ])

            print("Bot:", response)

            history.append("Bot: " + response)

            break

        # Check dictionary responses

        elif "hello" in user_input or "hi" in user_input:

            response = random_response("hello")

        elif "how are you" in user_input:

            response = random_response("how are you")

        elif "your name" in user_input:

            response = random_response("your name")

        elif "rational agent" in user_input:

            response = random_response("rational agent")

        elif "intelligent agent" in user_input:

            response = random_response("intelligent agent")

        elif "peas" in user_input:

            response = random_response("peas")

        elif "uniform cost" in user_input or "ucs" in user_input:

            response = random_response("ucs")

        elif "greedy best first" in user_input or "greedy" in user_input:

            response = random_response("greedy")

        elif "a*" in user_input or "a star" in user_input:

            response = random_response("a star")

        elif "bfs" in user_input:

            response = random_response("bfs")

        elif "dfs" in user_input:

            response = random_response("dfs")

        elif "what is ai" in user_input or user_input == "ai":

            response = random_response("ai")

        elif "what is ml" in user_input or user_input == "ml":

            response = random_response("ml")

        elif "what is dl" in user_input or user_input == "dl":

            response = random_response("dl")

        # Unknown input

        else:

            response = random.choice([
                "Sorry, I don't understand that yet.",
                "I'm still learning. Try typing 'help'.",
                "I don't have a rule for that question yet."
            ])

        print("Bot:", response)

        history.append("Bot: " + response)


# Start chatbot

chatbot()