class Answered(object):
    """keeps track of question and answer history.

    partof: #SPC-answered
    """

    def __init__(self):
        self._hist = {}

    def get_hist(self, question):
        """Return (num_right, num_wrong)."""
        self._hist.get(question.question, (0, 0))

    def record(self, question, correct):
        """Record question history."""
        before = self.get_hist(question)
        if correct:
            after = (before[0] + 1, before[1])
        else:
            after = (before[0], before[1] + 1)
        self._hist[question.question] = after

    def get_weights(self, questions):
        """Get the question weights based on answers.
        """
        total_right = sum(
            h[0] for h in self._hist.values())
        total_wrong = sum(
            h[1] for h in self._hist.values())

        weights = []
        for question in questions:
            hist = self.get_hist(question)
            weight = 1
            weight -= hist[0] / total_right
            weight += hist[1] / total_wrong
            weights.append(weight)

        return weights
class Question():
        
    def get_question(questions, answered):
        """Get a random question weighted by
        previous answers.

        partof: #SPC-quiz-get
        """
        weights = answered.get_weights(questions)
        return weighted_choice(weights, choices)


    def weighted_choice(weights, choices):
        """Get a choice randomly based on the weights.

        taken from:
            http://stackoverflow.com/questions/3679694

        partof: #SPC-random
        """
        total = sum(weights)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(choices, weights):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"