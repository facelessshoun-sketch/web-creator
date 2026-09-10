const API_BASE=localStorage.getItem("API_BASE")||"http://localhost:8000";
const promptBox=document.getElementById("prompt"),frame=document.getElementById("previewFrame"),statusBox=document.getElementById("status");
const setStatus=t=>statusBox.textContent=t;
document.querySelectorAll(".chips button").forEach(b=>b.onclick=()=>promptBox.value=b.dataset.prompt+". Make it modern, responsive and professional.");
document.getElementById("sampleBtn").onclick=()=>promptBox.value="Create a professional real-estate website called Innocent Group. Use red, blue and white. Add Home, Properties, About Us, Services and Contact sections. Make it modern, responsive and trustworthy.";
document.getElementById("generateBtn").onclick=async()=>{
 const prompt=promptBox.value.trim(); if(!prompt)return setStatus("Enter a description first.");
 setStatus("Generating website...");
 try{const r=await fetch(API_BASE+"/api/generate",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt})});
 const d=await r.json();if(!r.ok)throw Error(d.detail||"Generation failed");frame.srcdoc=d.html;setStatus("Website generated successfully.");}
 catch(e){setStatus("Error: "+e.message);}
};
document.getElementById("downloadBtn").onclick=async()=>{
 const prompt=promptBox.value.trim();if(!prompt)return setStatus("Enter a description first.");
 setStatus("Preparing ZIP...");
 try{const r=await fetch(API_BASE+"/api/download",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({prompt})});
 if(!r.ok)throw Error("Download failed");const blob=await r.blob(),url=URL.createObjectURL(blob),a=document.createElement("a");
 a.href=url;a.download="generated-website.zip";a.click();URL.revokeObjectURL(url);setStatus("ZIP downloaded.");}
 catch(e){setStatus("Error: "+e.message);}
};