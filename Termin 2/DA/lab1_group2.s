# Authors: 
# Jameel Saeed (jasa6359)
# Rasmus Rodriguez (raer3426)

.text
	.global _start

_start:
	movia	r17,0x10000000	# Address for the red LEDs
	movia	r18,0x10000010	# Address for the green LEDs
	
LOOP:
	movia	r9,0x4 # Initialize counter

ITERATE:
	subi	r9,r9,0x1 # subtract one from counter.
	call	TURN_ON_RED_LIGHTS
	bne		r9,r0, ITERATE # if r9 is not emptry, iterate.
	call	TURN_ON_GREEN_LIGHTS
	br		LOOP # call loop to reset counter.

TURN_ON_RED_LIGHTS:
	movia	r8,0x55555 # load "odd" pattern into r8.
	stwio	r8,0(r17) # copy "odd" pattern from r8 to r17 (adress in mem).
	stwio	r0,0(r17) # turn off all red LEDs.
	movia	r8,0xaaaaa # load "even" pattern into r8.
	stwio	r8,0(r17) # copy "even" pattern from r8 to r17 (adress in mem).
	stwio	r0,0(r17) # turn off all red LEDs.
	ret
	
TURN_ON_GREEN_LIGHTS:
	movia	r8,0x1ff # load pattern for all LEDs to light up to r8.
	stwio	r8,0(r18) # copy pattern from r8 to r17 (adress in mem)
	stwio	r0,0(r18) #  turn off all green LEDs.
	ret

END:
	break

.end
