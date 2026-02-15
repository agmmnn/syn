import React, { useEffect, useState } from "react";

interface ToastProps {
  message: string;
  visible: boolean;
}

export function Toast({ message, visible }: ToastProps) {
  return (
    <div className={`toast ${visible ? "visible" : ""}`}>
      {message}
    </div>
  );
}

export function useToast() {
  const [toast, setToast] = useState({ message: "", visible: false });

  const show = (message: string) => {
    setToast({ message, visible: true });
  };

  useEffect(() => {
    if (!toast.visible) return;
    const timer = setTimeout(() => {
      setToast((t) => ({ ...t, visible: false }));
    }, 1800);
    return () => clearTimeout(timer);
  }, [toast.visible, toast.message]);

  return { toast, show };
}
