import random

verbose = True


def log(text):
    if verbose:
        print(text)


class Prisoner():
    def __init__(self, number):
        self.number = number
        self.has_turned_on_lightbulb = False
        self.is_counter = False
        self.count = 1  # They always count themselves to start with

    def set_counter(self):
        self.is_counter = True

    def increment_count(self):
        self.count += 1

    def __str__(self):
        return "Prisoner {}\nLightbulb: {}\n\n".format(self.number, self.has_turned_on_lightbulb)

    def __repr__(self):
        return "Prisoner {}\nLightbulb: {}\n\n".format(self.number, self.has_turned_on_lightbulb)


def simulate(num_prisoners):
    lightbulb_on = False
    prisoners = [Prisoner(i+1) for i in range(num_prisoners)]
    prisoners[-1].is_counter = True
    prisoners_visited = set()
    visit_count = 0
    all_visited = False
    time_till_all_visited = 0

    while prisoners[-1].count < num_prisoners:
        visit_count += 1
        selected_prisoner = prisoners[random.randrange(num_prisoners)]
        prisoners_visited.add(selected_prisoner.number)
        if len(prisoners_visited) == num_prisoners and not all_visited:
            log("All prisoners have now entered the room.\n")
            time_till_all_visited = visit_count
            all_visited = True
        if selected_prisoner.is_counter:
            log("Counter enters the room, light is {}.".format(
                "ON" if lightbulb_on else "OFF"))
            if lightbulb_on:
                selected_prisoner.increment_count()
                lightbulb_on = False
                log("They count {} and turn the light back off.\n".format(
                    selected_prisoner.count))
            else:
                log("They do nothing.\n")
        else:
            log("Prisoner {} enters the room, light is {}.".format(
                selected_prisoner.number, "ON" if lightbulb_on else "OFF"))
            if not lightbulb_on and not selected_prisoner.has_turned_on_lightbulb:
                lightbulb_on = True
                selected_prisoner.has_turned_on_lightbulb = True
                log("They turn the light on.\n")
            else:
                if lightbulb_on:
                    log("They do nothing.\n")
                else:
                    log(
                        "They've already turned the light on before, so they do nothing.\n")
    log("Counter declares: 'Everyone has been here at least once!'")
    log("They are {}".format("correct!" if len(
        prisoners_visited) == num_prisoners else "WRONG!"))
    log("It took {} visits to the lightbulb room.".format(visit_count))
    log("However, all prisoners had visited the room after {} visits".format(
        time_till_all_visited))
    return visit_count, time_till_all_visited


trials = input("How many simulations? (<Enter> for Single) ")
number_of_prisoners = int(input("How many prisoners? "))
if trials == '':
    simulate(number_of_prisoners)
else:
    number_of_trials = int(trials)
    results = []
    results_all_visited = []

    verbose = number_of_trials <= 3
    for trial in range(number_of_trials):
        visit_count, all_visited = simulate(number_of_prisoners)
        results.append(visit_count)
        results_all_visited.append(all_visited)
        if number_of_trials < 1000:
            print("Trial {}: {} visits".format(trial+1, visit_count))
    print("\nAverage of {} trials with {} prisoners: {}".format(
        number_of_trials, number_of_prisoners, sum(results)/number_of_trials))
    print("Average number of visits till all prisoners had visited the room: {}".format(
        sum(results_all_visited)/number_of_trials))
