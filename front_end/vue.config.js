module.exports = {
  transpileDependencies: ['vuetify'],
  publicPath: process.env.NODE_ENV === 'production' ? "/dist" : "/",
  outputDir: "../back_end/dist/",
  devServer: {
    headers: {"Access-Control-Allow-Origin": "*"}
  }
}
