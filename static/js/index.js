const next = document.querySelector(".next");
const pre = document.querySelector(".pre");
const list = document.querySelector(".list");

let page = 1;
let items_per_page = 30;
let has_previous = false;
let has_next = false;

function add_data() {
    fetch(`http://127.0.0.1:8000/videos/${page}/${items_per_page}`)
        .then((res) => res.json())
        .then((res) => {
            has_previous = res.page.has_previous;
            has_next = res.page.has_next;

            let html = "";
            const videos = res.data;
            for (let i = 0; i < videos.length; i++) {
                const video = videos[i];

                html += `
                <a class="item" href="https://www.youtube.com/watch?v=${
                    video.video_id
                }"
                target="__blank"
                >
                <img src=${video.thumbnail}>
                <div class="texts">
                <div class="title">Title: ${video.title}</div>
                <div class="description">Description: ${
                    video.description.length > 40
                        ? video.description.substr(0, 40) + "..."
                        : video.description
                }</div>
                <div class="publish_time">Time: ${
                    new Date(video.publish_time).toString().split("GMT")[0]
                } </div>
                <div class="channel_title">Channel: ${video.channel_title}</div>
                </div> 
            </a> 
                
                `;
                list.innerHTML = html;
            }
        })
        .catch((e) => {
            console.log(e);
        });
}

next.addEventListener("click", (e) => {
    if (has_next) {
        page++;
        add_data();
    }
});

pre.addEventListener("click", (e) => {
    if (has_previous) {
        page--;
        add_data();
    }
});

add_data();
