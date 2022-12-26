import math

base_64_index = {'000000' :	 'A' ,'010000':'Q','100000':'g','110000':'w', '000001':'B','010001':'R','100001':'h','110001':'x', '000010':'C', '010010':'S','100010':'i','110010':'y','000011':'D','010011':'T','100011':'j','110011':'z','000100':'E','010100':'U','100100':'k','110100':'0','000101':'F','010101':'V','100101':'l','110101':'1','000110':'G','010110':   'W','100110':'m','110110':  '2', '000111':'H','010111':'X','100111':'n','110111':'3','001000':'I','011000'  :'Y','101000':'o','111000': '4','001001':'J','011001':  'Z','101001':'p','111001':  '5','001010':'K','011010': 'a','101010':'q', '111010':  '6','001011':'L','011011':'b','101011':'r','111011':  '7','001100':'M','011100':'c','101100':'s','111100':  '8','001101':   'N','011101':   'd','101101':   't','111101':'9','001110': 'O','011110':'e','101110':  'u','111110':'+','001111':'P', '011111':'f','101111':'v','111111':'/','Padding':'=' }
hex_bin_index = {'0':'0000','1':'0001','2':'0010','3':  '0011','4':'0100','5':  '0101','6':'0110','7':  '0111','8':'1000','9':  '1001','A':'1010','B':'1011','C':'1100','D': '1101','E':'1110','F' :'1111'}
ASCII_table = {'00':'NUL','01':'SOH','02':'STX','03':'ETX','04':'EOT','05':'ENQ','06':'ACK','07':'BEL','08':'BS','09':'HT','0A':'LF','0B':'VT','0C':'FF','0D':'CR','0E':'SO','0F':'SI','10':'DLE','11':'DC1','12':'DC2','13':'DC3','14':'DC4','15':'NAK','16':'SYN','17':'ETB','18':'CAN','19':'EM','1A':'SUB','1B':'ESC','1C':'FS','1D':'GS','1E':'RS','1F':'US','20':'space','21':'!','22':'"','23':'#','24':'$','25':'%','26':'&','27':"'",'28':'(','29':')','2A':'*','2B':'+','2C':',','2D':'-','2E':'.','2F':'/','30':'0','31':'1','32':'2','33':'3','34':'4','35':'5','36':'6','37':'7','38':'8','39':'9','3A':':','3B':';','3C':'<','3D':'=','3E':'>','3F':'?','40':'@','41':'A','42':'B','43':'C','44':'D','45':'E','46':'F','47':'G','48':'H','49':'I','4A':'J','4B':'K','4C':'L','4D':'M','4E':'N','4F':'O','50':'P','51':'Q','52':'R','53':'S','54':'T','55':'U','56':'V','57':'W','58':'X','59':'Y','5A':'Z','5B':'[','5C':'\\','5D':']','5E':'^','5F':'_','60':'`','61':'a','62':'b','63':'c','64':'d','65':'e','66':'f','67':'g','68':'h','69':'i','6A':'j','6B':'k','6C':'l','6D':'m','6E':'n','6F':'o','70':'p','71':'q','72':'r','73':'s','74':'t','75':'u','76':'v','77':'w','78':'x','79':'y','7A':'z','7B':'{','7C':'|','7D':'}','7E':'~','7F':'DEL'}


##ASCII TO HEX
def convert_string_to_hex(string):
    string_hex = ''
    hexa = []
    for i in range(len(string)):
        ordinal = ord(string[i])
        char_hex = hex(ordinal)
        char_hex = char_hex.replace('0x','')
        hexa.append(char_hex)
        string_hex = string_hex + char_hex
    return string_hex , hexa

##HEX TO ASCII
def convert_hex_to_ascii(hex_string):
    hex_list = list(hex_string)
    true_hexes = []
    doubler = 0
    hex_ = ''
    for i in range(len(hex_list)):
        hex_ = hex_ + hex_list[i].upper()
        doubler += 1
        if doubler == 2:
            true_hexes.append(hex_)
            hex_ = ''
            doubler = 0
    ascii_value = ''
    for true_hex in true_hexes:
        for k , v in ASCII_table.items():
            if true_hex == k:
                ascii_value += v
    return ascii_value

##BINARY TO HEX
def convert_binary_to_hex(binary_string):
    if len(binary_string) % 8 != 0:
        print('ERROR PROGRAM ONLY SUPPORTS 8-BYTE CHARACTER MAPPING')
        return
    binary_list = list(binary_string)
    x = 0
    nibbles = []
    nibble = ''
    for i in range(len(binary_list)):
        nibble = nibble + binary_list[i]
        x += 1
        if x == 4:
            nibbles.append(nibble)
            nibble = ''
            x = 0
    hex_string = ''
    hexes = []
    hex_ = ''
    for nibble in nibbles:
        for k ,v in hex_bin_index.items():
            if nibble == v:
                hex_ = hex_ + k
            if len(hex_) == 2:
                hex_string = hex_string + hex_
                hexes.append(hex_)
                hex_ = ''                
    return hexes , hex_string

    
def hex_to_decimal(hex_list):
    converted_hexes = []
    hex_key = {'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' :13 , 'E':14,'F':15}
    for hex_ in hex_list:
        x  = 0 
        hex_ = list(hex_)
        for char in hex_:
            char = char.upper()
            for k , v in hex_key.items():
                if char == k:
                    hex_[x] = str(v)
                    break
            x += 1
        hex_.reverse()
        converted_hexes.append(hex_)
    converted_hexes.reverse()
    column = 1
    decimal = 0
    for hex_ in converted_hexes:
        for num in hex_:
            dec = int(num) * column
            column = column * 16
            decimal = decimal + dec
    return decimal

def hex_to_binary(hex_list):
    bytes_ = []
    for hex_ in hex_list:
        byte = ''
        for digit in list(hex_):
            digit = digit.upper()
            for k , v in hex_bin_index.items():
                if str(digit) == k:
                    byte = byte + v
        bytes_.append(byte)
    return bytes_
        
def binary_to_base64(bits):
    binary = bits    
    x = 0
    b64_bin = ''.join(binary)
    sextets = [ ]
    sextet = ''
    sex = 1
    padding_count = 0
    while len(b64_bin) % 6 != 0:
        b64_bin = b64_bin + '0'
        padding_count = padding_count + 1
    padding_count = round(padding_count/2)
    for i in range(len(b64_bin)):
        sextet = sextet + str(b64_bin[i])
        if sex % 6 == 0:
            sextets.append(sextet)
            sex = 0
            sextet = ''
        sex = sex + 1
    base64 = ''
    for sextet in sextets:
        for k,v in base_64_index.items():
            if sextet == k:
                base64 = base64 + v
                break
    for i in range(padding_count):
        base64 = base64 + '='
    return base64

def base64_to_binary(base64):
    binary = ''
    for char in base64:
        for k , v in base_64_index.items():
            if char == v:
                binary = binary + k
                break
    padding = binary.split('P')
    binary = list(padding[0])
    padding_amount = padding.count('adding')
    binary.reverse()
    for i in range(padding_amount):
        del(binary[0])
        del(binary[1])
    binary.reverse()
    binary  = ''.join(binary)
    return binary
        
if __name__ == '__main__':
    while True:
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        conv= {}
        print('(A)SCII | BASE(2) | BASE(16) | BASE(64)')
        encoding = input('STRING ENCODING TYPE: ')

        if encoding == 'A' or encoding == 'a':
            string = input('INPUT ASCII TO ENCODE: ')
            base16 , hexa_ = convert_string_to_hex(string)
            base10 = hex_to_decimal(hexa_)
            base2_list = []
            base2 = hex_to_binary(hexa_)
            base64 = binary_to_base64(base2)
            conv['ASCII'] = string
            conv['BASE16'] = base16
            conv['BASE10'] = base10
            conv['BASE2'] = ''.join(base2)
            conv['BASE64'] = base64
            for thing in base2:
                base2_list.append(base2)
            for k , v in conv.items():
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('')
                print(k ,':' , v)
                print('')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            input('PRESS ANY KEY TO EXIT')

        if encoding == '16':
            hexa_ = input('ENTER HEX: ')
            string = convert_hex_to_ascii(hexa_)
            base10 = hex_to_decimal(hexa_)
            base2_list = []
            base2 = hex_to_binary(hexa_)
            base64 = binary_to_base64(base2)
            conv['ASCII'] = string
            conv['BASE16'] = hexa_
            conv['BASE10'] = base10
            conv['BASE2'] = ''.join(base2)
            conv['BASE64'] = base64
            for thing in base2:
                base2_list.append(base2)
            for k , v in conv.items():
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('')
                print(k ,':' , v)
                print('')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            input('PRESS ANY KEY TO EXIT')

        if encoding == '2':
            base2_list = []
            base2 = input('ENTER BINARY: ')
            hexa_ , hex_string = convert_binary_to_hex(base2)
            base10 = hex_to_decimal(hexa_)
            base64 = binary_to_base64(base2)
            string = convert_hex_to_ascii(hex_string)
            conv['ASCII'] = string
            conv['BASE16'] = hex_string
            conv['BASE10'] = base10
            conv['BASE2'] = ''.join(base2)
            conv['BASE64'] = base64
            for thing in base2:
                base2_list.append(base2)
            for k , v in conv.items():
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('')
                print(k ,':' , v)
                print('')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            input('PRESS ANY KEY TO EXIT')

        if encoding == '64':
            base2_list = []
            base64 = input('ENTER BASE64: ')
            base2 = base64_to_binary(base64)
            hexa_ , hex_string = convert_binary_to_hex(base2)
            base10 = hex_to_decimal(hexa_)
            string = convert_hex_to_ascii(hex_string)
            conv['ASCII'] = string
            conv['BASE16'] = hex_string
            conv['BASE10'] = base10
            conv['BASE2'] = ''.join(base2)
            conv['BASE64'] = base64
            for thing in base2:
                base2_list.append(base2)
            for k , v in conv.items():
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('')
                print(k ,':' , v)
                print('')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            input('PRESS ANY KEY TO EXIT')
