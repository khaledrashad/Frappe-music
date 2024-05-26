    let currentPage = 1;
    const pageSize = 10;

    async function loadSongs(page) {
        if (page < 1) return;

        const response = await fetch(`/api/method/music_app.www.songPortal.get_paginated_songs?page_number=${page}&page_size=${pageSize}`);
        const data = await response.json();
        const { songs, total_songs, page_number, page_size } = data.message;
        currentPage = page_number;

        const songsContainer = document.getElementById('songs-container');
        songsContainer.innerHTML = '';

        songs.forEach(song => {
            const songCard = `
                <div class="col-md-6">
                    <div class="songCard w-100 border border-3 p-2 m-2 text-center">
                        <img src="${song.song_image}" alt="Image of ${song.song_name}" class="w-75 img-fluid">
                        <h4 class="m-0 p-0">${song.artist}</h4>
                        <h3 class="m-0 p-0 text-info">${song.name}</h3>
                    </div>
                </div>
            `;
            songsContainer.innerHTML += songCard;
        });

        const totalPages = Math.ceil(total_songs / page_size);
        document.getElementById('page-info').innerText = `Page ${page_number} of ${totalPages}`;
        document.getElementById('prev-page').disabled = page_number === 1;
        document.getElementById('next-page').disabled = page_number === totalPages;
    }
    document.addEventListener('DOMContentLoaded', function() {
        loadSongs(currentPage);
    });