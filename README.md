## Texture synthesis of blood vessels for virtual surgery

#### Context

IITD and AIIMS have a collaborative project on building a neurosurgery simulator in VR for training of neurosurgery students. This requires building a realistic 3D model of the brain that the user can interact with in the simulation. The geometry of the brain can be obtained from CT/MRI scans and/or modeled by a skilled 3D artist, but the appearance is challenging to reproduce realistically. In particular the brain, like any other organ, has a complex network of blood vessels which can be seen in endoscopic images. Hence, we attempt to use the data from these images rather than generating similar networks of arbitrary sizes from scratch.

#### Problem Definition

We have many real photos and videos of the internal structures of the brain, captured during endoscopic surgical procedures. (i.e. The surgeons drill a hole in the skull and send in a camera and a surgical tool deep into the brain through a narrow tube.) We aim to use these images as exemplars to synthesize larger, illumination-free images that can be used as texture maps on the virtual brain geometry. This requires several steps: removing the illumination variation from the images; identifying relevant regions which contain only blood vessels and not other anatomical features; and finally, and example-based texture synthesis. .
