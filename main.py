from pyscript import document

def candidate_checker(e):
    club_members = [
        'brandon boyd',
        'jose pasillas',
        'dirk lance',
        'alex katunich',
        'chris killmore',
        'ben kenny',
        'mike einziger',
        'ben harper',
        'john mayer',
        'dave grohl',
        'taylor swift',
        'bruno mars',
        'hayley williams',
        'lenny kravitz'
    ]

    f_name = document.getElementById('first-name').value.strip()
    l_name = document.getElementById('last-name').value.strip()
    candidate = (f_name + ' ' + l_name).strip()
    member_checker = candidate.lower() in club_members

    messages = (
        f'Sorry, {f_name} is not a current member of the Music Club.',
        f'Congrats {f_name}, you now are a member of the Music Club!'
    )

    document.getElementById('result').innerText = messages[member_checker]