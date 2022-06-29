#Dictionary matching block of time to rate

hourlyRateBusinessDays = {
    ('00:00', '09:00'): 25,
    ('09:00', '18:00'): 15,
    ('18:00', '00:00'): 20,
}

hourlyRateWeekend = {
    ('00:00', '09:00'): 30,
    ('09:00', '18:00'): 20,
    ('18:00', '00:00'): 25,
}