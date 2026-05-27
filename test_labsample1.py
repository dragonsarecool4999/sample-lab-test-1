import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    sample = labsample1.get_longest_workout(workouts)
    answer = ({"date":"25.01.2022","activity":"Cycling","duration":75.0})
    assert(sample==answer)
def test_calc_total_duration():
    workouts = labsample1.load_csv()
    sample = labsample1.calc_total_duration(workouts)
    answer = 853.0
    assert(sample==answer)

def test_calc_average_duration():
    workouts = labsample1.load_csv()
    sample = labsample1.calc_average_duration(workouts)
    answer = 42.65
    assert(sample==answer)