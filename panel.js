const practicantes = [
    {
        nombre: "Juan Pérez",
        correo: "juan@example.com",
        carrera: "Ingeniería de Sistemas",
        semestre: 5,
        hoja_vida: "juan_hoja_vida.pdf",
        estado: "Pendiente"
    },
    {
        nombre: "Ana García",
        correo: "ana@example.com",
        carrera: "Ingeniería Industrial",
        semestre: 7,
        hoja_vida: "ana_hoja_vida.pdf",
        estado: "Pendiente"
    }
];

const tbody = document.querySelector("#practicantesList tbody");

practicantes.forEach((practicante, index) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
        <td>${practicante.nombre}</td>
        <td>${practicante.correo}</td>
        <td>${practicante.carrera}</td>
        <td>${practicante.semestre}</td>
        <td><a href="${practicante.hoja_vida}" target="_blank">Ver Hoja de Vida</a></td>
        <td>
            <button onclick="marcarEstado(${index}, 'Viable')">Viable</button>
            <button onclick="marcarEstado(${index}, 'No viable')">No viable</button>
        </td>
    `;

    tbody.appendChild(tr);
});

function marcarEstado(index, estado) {
    practicantes[index].estado = estado;
    alert(`${practicantes[index].nombre} ha sido marcado como ${estado}`);
    // Actualizar la interfaz del estado si es necesario
}
