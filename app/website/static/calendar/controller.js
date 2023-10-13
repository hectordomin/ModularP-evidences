document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('scheduler');
    var weeklyEvents = JSON.parse(calendarEl.getAttribute('data-weekly-events'));

    function updateCalendarView(calendar) {
        if (window.innerWidth <= 768) {
            calendar.changeView('listWeek'); // Vuelve a la vista semanal
            calendar.setOption('contentHeight', 650);
        } else {
            calendar.changeView('timeGridWeek'); // Cambia a vista diaria para tamaños pequeños
            calendar.setOption('contentHeight', 1000);
        }
    }

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'listWeek', // Muestra solo la vista semanal por defecto.
        locale: 'es',
        allDaySlot: false,
        slotMinTime: '07:00:00',
        slotMaxTime: '21:00:00',
        slotDuration: '01:00:00',
        slotLabelInterval: { hours: 1 },
        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit',
            omitZeroMinute: false,
            meridiem: false
        },
        expandRows: true,
        events: weeklyEvents,
        headerToolbar: false,
        hiddenDays: [0],
    });

    // Inicializa el calendario
    calendar.render();

    // Llama a la función para actualizar la vista basada en el tamaño de la pantalla
    updateCalendarView(calendar);

    // Agrega un evento de escucha para el cambio de tamaño de la ventana
    window.addEventListener('resize', function() {
        updateCalendarView(calendar);
    });
});
