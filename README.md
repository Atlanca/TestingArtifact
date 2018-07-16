## Purpose:
Write a flash card quizzer from scratch and learn about
quality best practices while doing so.

The example tutorial can be found here:
    http://wiki.openhatch.org/Flash_card_challenge

It should be easy for users to input questions to the
quizzer in a simple and open format. Additionally, the
quizzer should use effective memorization techniques. Some possible ideas
include:
- asking items in a random order
- telling the correct answer after the user answers incorrectly
- asking items more often if they were answered incorrectly
- allowing users to configure time limits, so they can
    compare results between quizzes.

### Requirements:
- REQ-display_questions: The system should display questions, so users know what to answer
- REQ-quiz_input: The system should be able to receive input in simple and open format, so users can answer given questions
- REQ-quiz_result: At the end of each quiz, the system should display which questions were answered correctly/incorrectly, so users can learn what they answered right or wrong
- REQ-random_order: The system shall be able to ask items in random order, so the user cannot just memorize question sequences
- REQ-show_correct_answer: The system shall be able to show the correct answer if the user answer is incorrect, so users can learn from mistakes
- REQ-same_type_questions: The system shall ask more questions of the same type if the previous answers to these questions were incorrect, so users can practice on question types they find - difficult
- REQ-time_limit: The system shall have a time limit for each question, to prevent users from looking around for answers
- REQ-time_limit_configuration: The system shall allow users to configure time limits, so they can compare results between quizzes.

### Specification per requirement:
- SPC-display_questions: The console should print the question being asked

- SPC-quiz_input: The console shall wait for user input

- SPC-quiz_result: The console shall print a list of questions that were answered, along with whether they were answered correct or not
- SPC-quiz_result: The system shall keep track of which questions were answered
- SPC-quic_result: The system shall keep track of whether answers to questions were correct or not
 
- SPC-random_order: The questions should have unique IDs, so they can easily be randomized
- 
- SPC-show_correct_answer: same as SPC-quiz_result
 
- SPC-same_type_questions: The system shall categorize questions by type
- SPC-same_type_questions: same as SPC-quiz_result
 
- SPC-time_limit: The system shall start a timer after a question has been asked
- SPC-time_limit: The system shall stop the user from providing input after time has elapsed
- SPC-time_limit: The system shall give a new question, or finish the quiz after the specified time has elapsed
 
- SPC-time_limit_configuration: The time limits in the system shall be adjustable 

### Required arguments for input:
- ARG-time_limit: Time limit for each question
- ARG-nbr_questions: Number of questions asked per quiz
- ARG-difficulty: Difficulty of quiz
- ARG-quiz_type: Optionally allow user to specify specific question types

