def solution(new_id):
    answer = ''
    #1단계
    new = new_id.lower()
    #2단계
    for i in new:
        if  i.isalnum() or i in '-_.':
            answer += i
    #3단계
    while '..' in answer:
        answer = answer.replace('..','.')
    #4단계
    answer = answer[1:] if answer[0] == '.' else answer
    #5단계
    answer = 'a' if answer == '' else answer
    #6단계
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    if len(answer) < 3:
        for i in range(len(answer),3):
            answer += answer[-1]  
    return answer