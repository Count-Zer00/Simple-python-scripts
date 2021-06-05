# converter just between omr and inr
choose = input("choose '1' for rupee to rial and '2' rial to rupee")

if choose == '1':
    def rial():
        rupee = int(input('input rupee to convert to rial: '))
        rial = rupee * 0.0053
        print(rial)
    rial()

if choose == '2':
    def rupee():
        rial = int(input('input rial to convert to rupee: '))
        rupee = rial * 188.45
        print(rupee)
    rupee()
