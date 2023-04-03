from rembg import remove

input_path = 'humming-dogs.jpg'
output_path = 'output.jpg'

with open(input_path, 'rb') as i_:
    with open(output_path, 'wb') as o_:
        out = remove(i_.read())
        o_.write(out)