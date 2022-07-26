#############################
# linear
###########################

_4 = MemRef("_4", 8, 8)
_4.zero()


@parfor(ranges=(range(0, 8, 1), range(0, 1, 1), range(0, 8, 1)))
def body(_arg3, _arg1, _arg2):
    fma = FMAC(_arg3, _arg1, _arg2)
    _7 = _arg0[_arg1, _arg3]
    _8 = _3[_arg3, _arg2]
    _9 = _4[_arg3, _arg2]
    _10 = examples.simple_nns.Mul(_7, _8)
    _11 = examples.simple_nns.Add(_9, _10)
    _4[_arg3, _arg2] = _11
    _4[_arg3, _arg2] = fma.Result(copy=False)


_4.registers = np.vstack([_4.registers, _2.registers])
_4.registers = np.apply_along_axis(ReduceAdd, 0, _4.registers)[np.newaxis]
Copy(_4, _4)
#############################
# linear
###########################


#############################
# conv
###########################


_5 = MemRef('_5', 2, 8, 9, 9)
_5.zero()


@parfor(_arg5=(0, 2, 1), _arg1=(0, 1, 1), _arg2=(0, 8, 1), _arg3=(0, 9, 1), _arg4=(0, 9, 1))
def body(_arg5, _arg1, _arg2, _arg3, _arg4):
    fma = FMAC(_arg5, _arg1, _arg2, _arg3, _arg4)
    for _arg6 in range(0, 3, 1):
        for _arg7 in range(0, 3, 1):
            _10 = _arg3 + _arg6
            _11 = _arg4 + _arg7
            _12 = _arg0[_arg1, _arg5, _10, _11]
            _13 = _3[_arg2, _arg5, _arg6, _arg7]
            _14 = _5[_arg5, _arg2, _arg3, _arg4]
            _15 = fma.Mul(_12, _13)
            _16 = fma.Add(_14, _15)
            _5[_arg5, _arg2, _arg3, _arg4] = _16
    _5[_arg5, _arg2, _arg3, _arg4] = fma.Result()


ReduceTiling(_5, _4)



#############################
# conv
###########################


#############################
# braggnn
###########################

_25 = MemRef('_25', 16, 8, 9, 9)
_25.zero()


@parfor(_arg5=(0, 16, 1), _arg1=(0, 1, 1), _arg2=(0, 8, 1), _arg3=(0, 9, 1), _arg4=(0, 9, 1))
def body(_arg5, _arg1, _arg2, _arg3, _arg4):
    fma = FMAC(_arg5, _arg1, _arg2, _arg3, _arg4)
    for _arg6 in range(0, 1, 1):
        for _arg7 in range(0, 1, 1):
            _74 = _arg3 + _arg6
            _75 = _arg4 + _arg7
            _76 = _23[_arg5, _arg5, _74, _75]
            _77 = _19[_arg2, _arg5, _arg6, _arg7]
            _78 = _25[_arg5, _arg2, _arg3, _arg4]
            _79 = fma.Mul(_76, _77)
            _80 = fma.Add(_78, _79)
            _25[_arg5, _arg2, _arg3, _arg4] = _80
    _25[_arg5, _arg2, _arg3, _arg4] = fma.Result()


ReduceTiling(_25, _24)