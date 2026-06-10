import json, datetime

path = '/mnt/e/My_Projects/晚安精選英語教學/data/entries.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

new_id = max(e['id'] for e in data) + 1

data.append({
    'id': new_id,
    'date': datetime.date.today().isoformat(),
    'phrase': 'It hits different',
    'meaning': '感覺特別不一樣、格外有感觸 — 形容某事帶給人的感受比平時更強烈或獨特',
    'category': 'slang',
    'tags': ['slang', 'social-media', 'internet', 'conversation', 'viral', 'enthusiasm'],
    'analysis': '「Hits different」是2025-2026年在社群平台上極度流行的俚語，字面意思是「打中方式不一樣」，用來形容某事物（音樂、食物、回憶、情感等）帶給你的感受特別強烈、與眾不同或格外觸動心弦。這個短語的妙處在於它傳達了主觀而難以言喻的體驗——不是好與壞的二分，而是一種「就是不太一樣」的獨特感受。它最早常見於粉絲圈討論歌曲（例如Taylor Swift的專輯《Hit Different》），後來擴展到日常生活各個層面。教學上可以讓學生對比「It is good」和「It hits different」的語氣差異——前者只是客觀評價，後者傳遞了個人情感連結，是非常實用的情感表達工具。',
    'examples': [
        'Listening to this song at midnight just hits different.',
        'Homemade bubble tea hits different — you cannot compare it to the store-bought ones.',
        'Seeing the sunset from the top of the mountain hits different when you hiked all the way up.'
    ]
})

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Saved entry #{new_id}')
with open(path, encoding='utf-8') as f:
    data2 = json.load(f)
last_entry = data2[-1]
print(f'Verified: id={last_entry["id"]}, phrase={last_entry["phrase"]}, examples count={len(last_entry["examples"])}')
