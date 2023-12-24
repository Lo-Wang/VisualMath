const canvas = document.querySelector("canvas")
const ctx = canvas.getContext("2d");
const ctx2 = canvas.getContext("2d");
canvas.width = 700;
canvas.height = 400;
const width = canvas.width;
const height = canvas.height;
const scaleX = 20;
const scaleY = 20;
const xAxis = Math.round(width / scaleX / 2) * scaleX;
const yAxis = Math.round(height / scaleY / 2) * scaleY;

let xCoord = [];
let yCoord = [];
const p = [{x:8*scaleX+xAxis,y:-5*scaleY+yAxis},{x:-8*scaleX+xAxis,y:5*scaleY+yAxis}];
var k = 0;
var b = 0;
var selectedVertex = null;
var ptx, pty = 0;
var text = '';

const alignment = 'left'; 
const left = alignment=='left';

function drawGrid() {
    ctx.beginPath();
    ctx.font = `${Math.round(scaleX/2)}px  Arial`;
    ctx.strokeStyle = 'rgba(0,0,0,0.5)';
    ctx.fillStyle ='rgba(0,0,0,0.5)';
    ctx.lineWidth = 1;
    for (var x = 0; x <= width; x += scaleX) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, height);
        ctx.fillText((x - xAxis)/scaleX, x+3, yAxis-3);
        xCoord.push(x);

    }
    for (var y = 0; y <= height; y += scaleY) {
        ctx.moveTo(0, y);
        ctx.lineTo(width, y);
        ctx.fillText((yAxis - y)/scaleY, xAxis+3, y-3);
        yCoord.push(y);
    }
    ctx.stroke();
    ctx.closePath();

    function drawLineWithArrowhead(p0,p1,headLength){

        // constants (could be declared as globals outside this function)
        var PI=Math.PI;
        var degreesInRadians225=225*PI/180;
        var degreesInRadians135=135*PI/180;

        // calc the angle of the line
        var dx0=p1.x-p0.x;
        var dy0=p1.y-p0.y;
        var angle=Math.atan2(dy0,dx0);

        // calc arrowhead points
        var x225=p1.x+headLength*Math.cos(angle+degreesInRadians225);
        var y225=p1.y+headLength*Math.sin(angle+degreesInRadians225);
        var x135=p1.x+headLength*Math.cos(angle+degreesInRadians135);
        var y135=p1.y+headLength*Math.sin(angle+degreesInRadians135);

        // draw line plus arrowhead
        ctx.beginPath();
        ctx.strokeStyle = "red";
        ctx.lineWidth = 2;
        // draw the line from p0 to p1
        ctx.moveTo(p0.x,p0.y);
        ctx.lineTo(p1.x,p1.y);
        // draw partial arrowhead at 225 degrees
        ctx.moveTo(p1.x,p1.y);
        ctx.lineTo(x225,y225);
        // draw partial arrowhead at 135 degrees
        ctx.moveTo(p1.x,p1.y);
        ctx.lineTo(x135,y135);
        // stroke the line and arrowhead
        ctx.stroke();
        ctx.closePath();
    }

    var p0={x:xAxis,y:height};
    var p1={x:xAxis,y:0};
    drawLineWithArrowhead(p0,p1,10);
    ctx.font = "21px Georgia";
    ctx.fillStyle = "red";
    ctx.fillText("y", p1.x-20, p1.y+15);
    p0={x:0,y:yAxis};
    p1={x:width,y:yAxis};
    drawLineWithArrowhead(p0,p1,10);
    ctx.fillText("x", p1.x-20, p1.y+15);
    ctx.closePath();
}


function drawLine(){
    clearcanvas()
    ctx.beginPath();
    ctx.arc(p[0].x,p[0].y,3,0,2*Math.PI,false);
    ctx.font = 'bold  15px  Arial';
    ctx.fillStyle ='blue';
    ctx.fillText("("+(p[0].x-xAxis)/scaleX+','+(yAxis-p[0].y)/scaleY+")", p[0].x-15, p[0].y+20);
    ctx.strokeStyle='blue';
    ctx.fill();
    ctx.stroke();
    ctx.closePath();

    ctx.beginPath();
    ctx.arc(p[1].x,p[1].y,3,0,2*Math.PI,false);
    ctx.font = 'bold 15px  Arial';
    ctx.fillStyle ='blue';
    ctx.fillText("("+(p[1].x-xAxis)/scaleX+','+(yAxis-p[1].y)/scaleY+")", p[1].x-20, p[1].y+20);
    ctx.strokeStyle='blue';
    ctx.fill();
    ctx.moveTo(p[1].x,p[1].y);
    ctx.lineTo(p[0].x,p[0].y);
    ctx.stroke();
    ctx.closePath();

    k, b = find_k_b(p);
    if (k == -1000 && b == -1000) {
      text = "y = "+ 0 +'; x = '+ (p[1].x-xAxis)/scaleX;
    }
    else if(b >= 0){
      text = "y = "+ k +'x+'+ b;}
    else if (b < 0){
      text = "y = "+ k +'x'+ b;
    }


    drawLabel(text, p);
}

function find_k_b(p){
  if ((((p[1].x-xAxis)/scaleX)-((p[0].x-xAxis)/scaleX)) == 0) {
    k = -1000;
    b = -1000;
    return (k,b);
  }
  else {
    k = Math.round((((yAxis-p[1].y)/scaleY)-((yAxis-p[0].y)/scaleY))/(((p[1].x-xAxis)/scaleX)-((p[0].x-xAxis)/scaleX))*100)/100;
    b = Math.round((((yAxis-p[0].y)/scaleY)-k*((p[0].x-xAxis)/scaleX))*100)/100;
    return (k,b);
  }
     
}

function drawLabel(text, g){
  var padding = 20;
  var dx = g[0].x - g[1].x;
  var dy = g[0].y - g[1].y; 
  var len = Math.sqrt(dx*dx+dy*dy);
  let angle1 = Math.atan2(dy,dx);
	if (angle1 < -Math.PI/2 || angle1  > Math.PI/2){
		var w = g[1];
		g[1] = g[0];
		g[0] = w;
		dx *= -1;
		dy *= -1;
    selectedVertex = Math.abs(selectedVertex-1)
		angle1 -= Math.PI;
    console.log('после',angle1)
    console.log(g)
	}

  let t0, pad;
	t0 = left ? g[1] : g[0];
	pad = padding / len * (left ? 1 : -1);

  ctx.save();
  ctx.beginPath();
  ctx.textAlign = alignment;
  ctx.translate(t0.x+dx*pad,t0.y+dy*pad);
  ctx.rotate(angle1);
  ctx.font = 'bold 20px  Arial';
  ctx.fillText(text,5,-5);
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
  ctx.restore();

}

function clearcanvas()
{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawGrid();
}

// Проверяет насколько близко курсор мыши
function checkVertexSelection_2(x, y) {
  for (var i = 0; i < xCoord.length; i++) {
    const distance = Math.abs(x - xCoord[i]);
    if (distance <= 5) {
      ptx = xCoord[i];
    }
  }
  for (var i = 0; i < yCoord.length; i++) {
    const distance = Math.abs(y - yCoord[i]);
    if (distance <= 5) {
      pty = yCoord[i];
    }
  }
  return(ptx,pty);
 }

  function checkVertexSelection(x, y) {
    for (let i = 0; i < p.length; i++) {
      const vertex = p[i];
      const distance = Math.sqrt((x - vertex.x) ** 2 + (y - vertex.y) ** 2);
      if (distance < 5) {
        selectedVertex = i;
        return;
      }
    }
    selectedVertex = null;
  }


  // Добавляем реакцию на клик мыши по холсту
  canvas.addEventListener("mousedown", (e) => {
    const xcli = e.clientX - canvas.getBoundingClientRect().left;
    const ycli = e.clientY - canvas.getBoundingClientRect().top;

    checkVertexSelection(xcli, ycli);
      // Следим за перемещениями мыши и другими действиями
      // в частности за перемещением вершины при удержании лкм
      // и завершением перемещения 
    canvas.addEventListener("mousemove", moveVertex);
    canvas.addEventListener("mouseup", () => {
      canvas.removeEventListener("mousemove", moveVertex);
    });
  });
  // Обрабатываем перемещение вершины
  function moveVertex(e) {
    const k = e.clientX - canvas.getBoundingClientRect().left;
    const l = e.clientY - canvas.getBoundingClientRect().top;

    ptx, pty = checkVertexSelection_2(k, l);

    if (selectedVertex !== null) {
      p[selectedVertex].x = ptx;
      p[selectedVertex].y = pty;
      drawLine();
    }
  }

// для начальной отрисовки пустой сетки
drawGrid();
drawLine();
