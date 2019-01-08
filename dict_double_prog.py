faisal = {'username': 'sfaisal', 'online': True, 'students': 145, 'section':'Computer Science', 'experience in years':21}
farhan = {'username': 'farhanahmed', 'online': False, 'students': 144, 'section':'Software Engineering', 'experience in years':15}

for common_key in faisal.keys() & farhan.keys():
    print("The value from Faisal is:", faisal[common_key], " and from Farhan is:",farhan[common_key])
