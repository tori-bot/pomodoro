
let submitBtn = document.querySelector('#submit')

//DOM
let daysDiv = document.getElementById('days')
let hoursDiv = document.getElementById('hours')
let minsDiv = document.getElementById('mins')
let secsDiv = document.getElementById('secs')



let countDownFunc = setInterval(function(){
  let time = 10
  let countDownTo = new Date().getTime() + (time*60*1000)
  let timeNow = new Date().getTime()
  timeleft = countDownTo - timeNow

  let days = Math.floor(timeleft/(1000*60*60*24))
  let hours = Math.floor((timeleft % (1000*60*60*24))/(1000*60*60))
  let mins = Math.floor((timeleft % (1000*60*60))/(1000*60))
  let secs = Math.floor((timeleft % (1000*60)/1000))
  daysDiv.innerHTML = days +' days'
  hoursDiv.innerHTML = hours + ' hours'
  minsDiv.innerHTML = mins+ ' mins'
  secsDiv.innerHTML = secs+' secs'

}, 1000)


countDownFunc()
