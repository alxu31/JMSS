% MODEL 1: referenceArea = pi*r^2, blade velo = (rpm/60)*2*pi -> angular
% velocity

% Bell 206 Jet Ranger
% Define constants
% lift = 1/2*(airDensity*(velo**2)*referenceArea*liftCoefficient)
% airResistance = 1/2*(airDensity*v^2*dragCoefficient*crossArea)
% airDensity = (101.29*((15.04-0.00649*r+273.1)/288.08)^(5.256))/(0.2869*(15.04-0.00649*r+273.1));
bladeDiameter = 10.15;
rpm = 394; % approx 394
passengers = 1; % 1-5
emptyMass = 730;
mass = emptyMass + (passengers*62); % avg weight of person = 62
velo = (rpm/60)*2*pi; % Not sure if angular velo or avg velo or get all sep lifts and add them

referenceArea = pi*((bladeDiameter/2)^2);
liftCoefficient = 0.12;

G = 6.67430e-11;
mEarth = 5.9722e24;
rEarth = 6371000;

dragCoefficient = 1; % approx 0.8 - 1.2
crossArea = 15.12;

% Time
t_start = 0;
t_end = 1800; % Change for diff time intervals
dt = 0.1;
time = t_start:dt:t_end;

% Init arrays for pos, velo, and accel
num_steps = length(time);
r = zeros(1, num_steps); % Pos
v = zeros(1, num_steps); % Velo
accel = zeros(1, num_steps); % Accel

% Init conditions
r(1) = 0;
v(1) = 0;

% Computes acceleration and displacement over time
for i = 2:num_steps
    % Fnet = ma -> Accel = (lift-weight-airResistance)/mass
    
    airDensity = (101.29*((15.04-0.00649*r(i-1)+273.1)/288.08)^(5.256))/(0.2869*(15.04-0.00649*r(i-1)+273.1));
    airResistance = 1/2*(airDensity*(v(i-1)^2)*dragCoefficient*crossArea);
    
    accel(i) = ((1/2*(airDensity*(velo^2)*referenceArea*liftCoefficient))-(G*((mass*mEarth)/((r(i-1)+rEarth)^2)))-airResistance)/mass;
    
    v(i)=v(i-1)+accel(i)*dt;
    r(i)=r(i-1)+v(i)*dt;
end

% Plotting
figure;

subplot(3,1,1);
plot(time, accel);
title('Acceleration vs. Time');
xlabel('Time (s)');
ylabel('Acceleration (m/s^2)');

subplot(3, 1, 2);
plot(time, v);
xlabel('Time step');
ylabel('Velocity (m/s)');
title('Velocity vs. Time');

subplot(3,1,3);
plot(time, r);
title('Displacement vs. Time');
xlabel('Time (s)');
ylabel('Displacement (m)');

sgtitle('Helicopter Vertical Motion');
