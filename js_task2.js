var data=[{Principal: 2500, time: 1.8}, {Principal: 1000, time: 5}, 
{Principal: 3000, time: 1},{ Principal: 2000, time: 3}];

interestCalculator()

function interestCalculator(){
 var rate;
 var interest;
 var interestData = [];

for( var i = 0; i < 4; i++ ){ 
 if (data[i].Principal >= 2500 && 1 < data[i].time < 3){
 rate = 3;
 
 }

else if (data[i].Principal >= 2500 &&  data[i].time >= 3){
rate = 4;

}
else if (data[i].Principal < 2500 && data[i].time == 1){
rate = 2;

}
else {rate=1;
}

interest = (data[i].Principal * rate * data[i].time) / 100 ;

interestData[i]={};

interestData[i].Principal = data[i].Principal;
interestData[i].Rate= rate;
interestData[i].Time= data[i].time;
interestData[i].Interest= interest;

}
console.log(interestData);
return interestData;
}
