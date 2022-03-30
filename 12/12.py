data = None
with open('evil2.gfx','rb') as f:
    data=f.read()
c = 0
for index in range(0,5):
    split_data = data[index:len(data):5]
    with open(str(index) + '.jpg', 'wb') as f:
        f.write(split_data)