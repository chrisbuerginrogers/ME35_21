
#include "Wioterminal.h"

Wioterminal test(115200);

void setup() {
  test.start();
}

void loop() {
   test.lookout();
}
