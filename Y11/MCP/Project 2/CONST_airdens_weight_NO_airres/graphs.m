% Define constants
% lift = 1/2*(airDensity*(velo**2)*referenceArea*liftCoefficient)
% airDensity = (101.29*((15.04-0.00649*r+273.1)/288.08)^(5.256))/(0.2869*(15.04-0.00649*r+273.1));
bladeDiameter = 10.15;
g = 9.8;
rpm = 394;
passengers = 1; % 1-5
emptyMass = 730;
mass = emptyMass + (passengers*62); % avg weight of person = 62
velo = (rpm/60)*2*pi;

referenceArea = pi*((bladeDiameter/2)^2);
liftCoefficient = 0.12;
weight = mass*g;

% Time
t_start = 0;
t_end = 100000; % Change for diff time intervals
dt = 0.1;
time = t_start:dt:t_end;

% Init arrays for pos, velo, and accel
num_steps = length(time);
r = zeros(1, num_steps);     % Pos
accel = zeros(1, num_steps); % Accel

% Init conditions
r(1) = 0;

% Computes acceleration and displacement over time
for i = 2:num_steps
    % Fnet = ma -> Accel = (lift-weight)/mass
    accel(i) = ((1/2 * (((101.29 * ((15.04 - 0.00649 * r(i-1) + 273.1) / 288.08)^(5.256))/(0.2869*(15.04-0.00649*r(i-1)+273.1))) * (velo^2) * referenceArea * liftCoefficient)) - weight) / mass;
    
    r(i) = r(i-1) + 0.5 * accel(i) * dt^2;
end

% Velo derivative of acceleration
velo_time = cumsum(accel) * dt;

% Plotting
figure;

subplot(3,1,1);
plot(time, accel);
title('Acceleration vs. Time');
xlabel('Time (s)');
ylabel('Acceleration (m/s^2)');

subplot(3,1,2);
plot(time, velo_time);
title('Velocity vs. Time');
xlabel('Time (s)');
ylabel('Velocity (m/s)');

subplot(3,1,3);
plot(time, r);
title('Displacement vs. Time');
xlabel('Time (s)');
ylabel('Displacement (m)');

sgtitle('Helicopter Vertical Motion');
