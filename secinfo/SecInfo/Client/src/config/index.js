var isPro = process.env.NODE_ENV === 'production'
module.exports = {
    baseURL: isPro ? '/' : 'http://127.0.0.1:9999/'
}
