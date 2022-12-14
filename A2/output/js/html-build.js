/* written by Tim McGinley 2022 */
/* And edited by Group 3 */

// ok in here we need to include a lot of stuff.
// we need a menu... where would this fit?
// we need to start (over)loading stuff into the DOM.
// we need to split the screen into section and plan and KPIs and info - where should this go?


function main() {

	// calculate the floors
	const floors = document.getElementsByTagName("floor-");
	let num_floors = floors.length;
	console.log(num_floors);
	
	// Total windows and window area - added by group3
	const windows = document.getElementsByTagName("window-");
	let num_windows = windows.length;
	console.log(num_windows);


	// add data to the properties box
	$('props-').prepend('number of floors is '+num_floors)+'<br>';
	$('props-').prepend('site elevation is '+$('site-').attr('elev')+'<br>');
	//Added by group 3
	$('props-').prepend('Total number of windows is '+num_windows+'<br>');
  $('props-').prepend('Total window area is ' + $('AreaOfWindows-').attr('TotalArea').bold() + ' m2'.bold() +'<br>');

	// load the plan so we can edit it
	plan('Now we are in control');

	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			//  Modified by group 3
			changePlan($(this).attr('name')+':'+$(this).attr('level') + '<br>' + 'Window Area of floor: ' + $(this).attr('WindowAreaByFloor') + 'm2');
			//$( this ).innerHTML
		});
	});


}

function plan(text) {
jQuery('<div>', {
    id: 'plan',
    class: 'plan',
    title: 'click a floor to see the plan',
	html:text
}).appendTo('plan-');

}

function changePlan(text) {
	$('#plan').html(text);
}





// <project-> - title etc.... | <site-> - also menu? site specific data?
// ---------------------------------------------------------------------
// <building-> - name of the building? this then needs to split in two...
// could also be more views and show a 3d? but maybe left is consistent
// ---------------------------------------------------------------------
// #section                   |               #plan
// this shows the floors      |      this shows a floor in plan         |
// in section                 |                 #plan                   |
//    <floor...->              -----------------------------------------
//                            |                 <properties->           |
// ---------------------------------------------------------------------
