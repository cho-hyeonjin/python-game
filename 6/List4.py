animals = ["🐶", "🐷", "🐯", "🐰", "🐭", "🐸", "🐱", "🐻", "🐹", "🦊", "🐨", "🐵", "🦁"]
print (animals, "=> 총", len(animals), "종류의 동물이 리스트에 있습니다.")

# 요소 추가, 제거, 배열 병합
animals.append("🐮") # 추가
print (animals, "=> 총", len(animals), "종류의 동물이 리스트에 있습니다.")
animals.pop(-1) # 제거 --> 인덱스 이용 : arr.pop(인덱스)

animals2 = ["🐮", "🐼"] # 여러 개 한 번에 추가하고 싶으면 새 배열에 담아서 확장
animals.extend(animals2) # 배열 병합
print (animals, "=> 총", len(animals), "종류의 동물이 리스트에 있습니다.")
animals.remove("🐼") # 제거 --> 요소값 이용: arr.remove(요소값)
print (animals, "=> 총", len(animals), "종류의 동물이 리스트에 있습니다.")
