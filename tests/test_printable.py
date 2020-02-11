from lawu import constants


def test_printable_constants():
    # Ensure we can successfully repr valid constants without crashing.
    pool = constants.ConstantPool()
    repr(constants.UTF8(pool=pool, value='HelloWorld'))
    repr(constants.ConstantClass(pool=pool, name='HelloWorld'))
    repr(constants.Double(pool=pool, value=1))
    repr(constants.Integer(pool=pool, value=1))
    repr(constants.Long(pool=pool, value=1))
