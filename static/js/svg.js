let groups = document.getElementsByTagName("g");
for (let i = 0; i < groups.length; i++) {
  const group = groups[i];
  group.addEventListener("click", (e) => {
    e.stopPropagation();
    let target_muscle = e.target.parentNode.getAttribute("muscle_id");
    let link = "/tutorial/" + target_muscle;
    window.open(link);
  });
}

