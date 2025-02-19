import { useEffect, useRef, useState } from "react";

function Ad() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [lastTime, setLastTime] = useState(0);

  useEffect(() => {
    const videoElement = videoRef.current;

    if (!videoElement) {
      return;
    }

    videoElement.controls = false;

    const handleTimeUpdate = () => {
      if (videoElement.currentTime > lastTime + 0.1) {
        videoElement.currentTime = lastTime;
      } else {
        setLastTime(videoElement.currentTime);
      }
    };

    const handleContextMenu = (event: MouseEvent) => {
      event.preventDefault();
    };

    videoElement.addEventListener("timeupdate", handleTimeUpdate);
    videoElement.addEventListener("contextmenu", handleContextMenu);

    return () => {
      videoElement.removeEventListener("timeupdate", handleTimeUpdate);
      videoElement.removeEventListener("contextmenu", handleContextMenu);
    };
  }, [lastTime]);

  return (
    <div>
      <video id="ad-video" ref={videoRef} autoPlay>
        <source src="ad-video-source.mp4" type="video/mp4" />
        Ваш браузер не поддерживает видео.
      </video>
    </div>
  );
}

export default Ad;
