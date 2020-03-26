var divs = $('div[id^="content-"]').hide();
var phases = $('h1[id^="phase-"]').hide();
var i = 0;
$(divs.eq(i)).show();
$(phases.eq(i)).show();

function next() {
  if (i == 4) {
    $(divs.eq(i)).hide();
    $(divs.eq(i)).fadeIn(1000);
  } else {
    $(divs.eq(i)).hide();
    $(phases.eq(i)).hide();
    i = ++i % divs.length;
    $(phases.eq(i)).fadeIn(500);
    $(divs.eq(i)).fadeIn(1000);
  }
}

function previous() {
  if (i == 0) {
    $(divs.eq(i)).hide();
    $(divs.eq(i)).fadeIn(1000);
  } else {
    $(divs.eq(i)).hide();
    $(phases.eq(i)).hide();
    i = --i % divs.length;
    $(phases.eq(i)).fadeIn(500);
    $(divs.eq(i)).fadeIn(1000);
  }
}
