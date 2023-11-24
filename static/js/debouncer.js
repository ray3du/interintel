/**
 * @Param {Function} callback
 * @Param {Number} delay
 * @Return {Function}
 * */
const Debouncer = (callback, delay) => {
    let timer;
    return (...args) => {
        let context = this
        clearTimeout(timer)

        timer = setTimeout(() => {
            callback.apply(context, args)
        }, delay)
    }
}